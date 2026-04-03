// Режим доступности (пока без озвучки)
let accessibilityMode = true;
let speechEnabled = true;
let activeUtterance = null;
let hoverSpeakTimer = null;
let selectedVoice = null;

const INTERACTIVE_SELECTOR = 'a, button, select, [role="button"], [role="link"], [data-speak], input[type="button"], input[type="submit"], input[type="reset"]';

function getVoiceIndicator() {
    return document.getElementById('voiceIndicator');
}

function showVoiceIndicator(message) {
    const indicator = getVoiceIndicator();
    if (!indicator) {
        return;
    }

    const textNode = indicator.querySelector('span:last-child');
    if (textNode) {
        textNode.textContent = message || 'Озвучивание...';
    }

    indicator.classList.add('active');
}

function hideVoiceIndicator() {
    const indicator = getVoiceIndicator();
    if (!indicator) {
        return;
    }

    indicator.classList.remove('active');
}

function normalizeSpeechText(text) {
    if (!text) {
        return '';
    }

    return text
        .replace(/YouTube/gi, 'Ютуб')
        .replace(/PDF/gi, 'П Д Ф')
        .replace(/IT/gi, 'ай ти')
        .replace(/FAQ/gi, 'частые вопросы')
        .replace(/[→←↔↗↘⇢➜]/g, ' ')
        .replace(/[\u{1F300}-\u{1FAFF}]/gu, ' ')
        .replace(/[\u2600-\u27BF]/g, ' ')
        .replace(/\s+/g, ' ')
        .trim();
}

function inferElementLabel(element) {
    if (!element) {
        return '';
    }

    if (element.id === 'prevBtn') {
        return 'Предыдущая страница';
    }

    if (element.id === 'nextBtn') {
        return 'Следующая страница';
    }

    if (element.id === 'accessibilityModeBtn') {
        return 'Переключить русское озвучивание';
    }

    if (element.classList.contains('modal-close')) {
        return 'Закрыть окно';
    }

    if (element.classList.contains('btn-download')) {
        return 'Скачать материал';
    }

    if (element.classList.contains('btn-view')) {
        return 'Открыть материал';
    }

    return '';
}

function getSpeakableText(element) {
    if (!element) {
        return '';
    }

    if (element.tagName === 'SELECT') {
        const label = document.querySelector(`label[for="${element.id}"]`);
        const selectedOption = element.options[element.selectedIndex];
        const selectText = `${label ? label.textContent : 'Фильтр'}: ${selectedOption ? selectedOption.textContent : element.value}`;
        return normalizeSpeechText(selectText);
    }

    const explicitText = element.getAttribute('data-speak')
        || element.getAttribute('aria-label')
        || element.getAttribute('title')
        || element.getAttribute('placeholder')
        || element.value
        || element.alt
        || element.textContent
        || inferElementLabel(element);

    return normalizeSpeechText(explicitText) || inferElementLabel(element);
}

function updateVoiceSelection() {
    if (!('speechSynthesis' in window)) {
        return;
    }

    const voices = window.speechSynthesis.getVoices();
    if (!voices.length) {
        return;
    }

    selectedVoice = voices.find((voice) => voice.lang && voice.lang.toLowerCase().startsWith('ru'))
        || voices.find((voice) => voice.name && /russian|рус/i.test(voice.name))
        || voices[0];
}

function stopSpeaking() {
    clearTimeout(hoverSpeakTimer);

    if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
    }

    activeUtterance = null;
    document.querySelectorAll('.speaking').forEach((element) => element.classList.remove('speaking'));
    hideVoiceIndicator();
}

function speakText(text, element) {
    const phrase = normalizeSpeechText(text);
    if (!speechEnabled || !phrase || !('speechSynthesis' in window)) {
        return;
    }

    stopSpeaking();
    updateVoiceSelection();

    const utterance = new SpeechSynthesisUtterance(phrase);
    utterance.lang = selectedVoice?.lang || 'ru-RU';
    utterance.voice = selectedVoice || null;
    utterance.rate = 1;
    utterance.pitch = 1;
    utterance.volume = 1;

    utterance.onstart = () => {
        if (element) {
            element.classList.add('speaking');
        }
        showVoiceIndicator(phrase);
    };

    utterance.onend = () => {
        if (element) {
            element.classList.remove('speaking');
        }
        hideVoiceIndicator();
        activeUtterance = null;
    };

    utterance.onerror = () => {
        if (element) {
            element.classList.remove('speaking');
        }
        hideVoiceIndicator();
        activeUtterance = null;
    };

    activeUtterance = utterance;
    window.speechSynthesis.speak(utterance);
}

function speakElement(element) {
    const text = getSpeakableText(element);
    if (!text) {
        return;
    }

    hoverSpeakTimer = window.setTimeout(() => {
        speakText(text, element);
    }, 120);
}

function attachSpeechHandlers(root = document) {
    root.querySelectorAll(INTERACTIVE_SELECTOR).forEach((element) => {
        if (element.dataset.voiceBound === 'true') {
            return;
        }

        element.dataset.voiceBound = 'true';
        element.addEventListener('mouseenter', () => speakElement(element));
        element.addEventListener('focus', () => speakElement(element));
        element.addEventListener('change', () => speakElement(element));
        element.addEventListener('mouseleave', stopSpeaking);
        element.addEventListener('blur', stopSpeaking);
    });
}

function attachDataHrefHandlers(root = document) {
    root.querySelectorAll('[data-href]').forEach((element) => {
        if (element.dataset.linkBound === 'true') {
            return;
        }

        element.dataset.linkBound = 'true';
        element.addEventListener('click', (event) => {
            if (event.target.closest('a, button') && event.target !== element) {
                return;
            }

            const targetUrl = element.dataset.href;
            if (targetUrl) {
                window.location.href = targetUrl;
            }
        });

        element.addEventListener('keydown', (event) => {
            if (event.key !== 'Enter' && event.key !== ' ') {
                return;
            }

            event.preventDefault();
            const targetUrl = element.dataset.href;
            if (targetUrl) {
                window.location.href = targetUrl;
            }
        });
    });
}

function announceModeState() {
    const message = accessibilityMode
        ? 'Русское озвучивание включено'
        : 'Русское озвучивание выключено';
    speakText(message);
}

function toggleAccessibilityMode() {
    accessibilityMode = !accessibilityMode;
    speechEnabled = accessibilityMode;

    const btn = document.getElementById('accessibilityModeBtn');
    if (btn) {
        btn.classList.add('switching');
        setTimeout(() => {
            btn.classList.remove('switching');
        }, 600);
    }

    document.body.classList.toggle('accessibility-mode', accessibilityMode);
    localStorage.setItem('accessibilityMode', accessibilityMode ? 'true' : 'false');
    localStorage.setItem('speechEnabled', speechEnabled ? 'true' : 'false');
    announceModeState();
    document.dispatchEvent(new CustomEvent('accessibility-mode-changed', { detail: { enabled: accessibilityMode } }));
}

function checkSavedMode() {
    const savedAccessibilityMode = localStorage.getItem('accessibilityMode');
    const savedSpeechEnabled = localStorage.getItem('speechEnabled');

    // По умолчанию включено, если пользователь еще не выбирал режим
    accessibilityMode = savedAccessibilityMode === null
        ? true
        : savedAccessibilityMode === 'true';

    speechEnabled = savedSpeechEnabled === null
        ? accessibilityMode
        : savedSpeechEnabled === 'true';

    document.body.classList.toggle('accessibility-mode', accessibilityMode);

    // Синхронизируем хранилище для всех страниц
    localStorage.setItem('accessibilityMode', accessibilityMode ? 'true' : 'false');
    localStorage.setItem('speechEnabled', speechEnabled ? 'true' : 'false');

    document.dispatchEvent(new CustomEvent('accessibility-mode-changed', {
        detail: { enabled: accessibilityMode }
    }));
}

document.addEventListener('DOMContentLoaded', () => {
    checkSavedMode();
    updateVoiceSelection();
    attachSpeechHandlers();
    attachDataHrefHandlers();
    
    // Sayt ochilganda rejim haqida xabar berish
    if (accessibilityMode && speechEnabled) {
        showVoiceIndicator('Русское озвучивание готово');
        // Kichik kutish bilan ovozli xabar
        window.setTimeout(() => {
            speakText('Русское озвучивание включено. Наведите курсор на элементы для озвучивания');
            window.setTimeout(hideVoiceIndicator, 3000);
        }, 500);
    } else {
        showVoiceIndicator('Русское озвучивание готово');
        window.setTimeout(hideVoiceIndicator, 1400);
    }
});

if ('speechSynthesis' in window) {
    window.speechSynthesis.onvoiceschanged = updateVoiceSelection;
}
