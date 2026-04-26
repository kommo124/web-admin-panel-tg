const messageInput = document.getElementById('messageInput')
const messageInputAll = document.getElementById('messageInputAll')
const sendBtn = document.getElementById('sendBtn')
const sendBtnAll = document.getElementById('sendBtnAll')
const chatIdInput = document.getElementById('messageChatIdInput')
const tokenInput = document.getElementById("tokenInput")

// ===== Работа с токеном =====
if (tokenInput) {
    const savedToken = localStorage.getItem('bot_token')
    if (savedToken) tokenInput.value = savedToken

    tokenInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            localStorage.setItem('bot_token', tokenInput.value.trim())
        }
    })

    tokenInput.addEventListener('blur', () => {
        localStorage.setItem('bot_token', tokenInput.value.trim())
    })
}

// ===== Отправка одному =====
sendBtn.addEventListener('click', async (e) => {
    e.preventDefault()

    const tokenVal = tokenInput.value.trim()
    const messageInputVal = messageInput.value.trim()
    const chatIdInputVal = parseInt(chatIdInput.value)

    if (!chatIdInputVal || !messageInputVal || !tokenVal) {
        alert("Заполните все поля")
        return
    }

    try {
        const response = await fetch('http://localhost:8000/send', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                chat_id: chatIdInputVal,
                text: messageInputVal,
                token: tokenVal
            })
        })

        const result = await response.json()
        console.log('Сообщение отправлено:', result)
    } catch (error) {
        console.error('Ошибка:', error)
    }
})

// ===== Отправка всем =====
sendBtnAll.addEventListener('click', async (e) => {
    e.preventDefault()

    const tokenVal = tokenInput.value.trim()
    const messageInputAllVal = messageInputAll.value.trim()

    if (!messageInputAllVal || !tokenVal) {
        alert("Введите сообщение и токен")
        return
    }

    try {
        const response = await fetch('http://localhost:8000/sendAll', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                text: messageInputAllVal,
                token: tokenVal
            })
        })

        const result = await response.json()
        console.log('Сообщение отправлено всем:', result)
    } catch (error) {
        console.error('Ошибка:', error)
    }
})

// ===== Статистика =====
async function loadTotalUsers() {
    const totalElement = document.getElementById('totalUsers')

    try {
        const response = await fetch("http://localhost:8000/stats")
        const data = await response.json()

        if (data.total_users !== undefined) {
            totalElement.textContent = data.total_users
        }
    } catch (error) {
        console.error('Ошибка:', error)
    }
}

window.addEventListener("load", loadTotalUsers)
setInterval(loadTotalUsers, 10000)