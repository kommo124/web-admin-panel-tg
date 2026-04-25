const messageInput = document.getElementById('messageInput')
const messageInputAll = document.getElementById('messageInputAll')

const sendBtn = document.getElementById('sendBtn')
const sendBtnAll = document.getElementById('sendBtnAll')

const chatIdInput = document.getElementById('messageChatIdInput')

sendBtn.addEventListener('click', async (e) => {
    e.preventDefault()
    const messageInputVal = messageInput.value
    const chatIdInputVal = parseInt(chatIdInput.value)

    if (!chatIdInputVal || !messageInputVal) {
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
                text: messageInputVal
            })
        })

        const result = await response.json()
        console.log('Сообщение успешно отпарвлено, проверьте чат с ботом')


    } catch (error) {
        console.error('Ошибка: ', error)
    }

})

sendBtnAll.addEventListener('click', async (e) => {
    e.preventDefault()
    const messageInputAllVal = messageInputAll.value

    try {
        const response = await fetch('http://localhost:8000/sendAll', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },

            body: JSON.stringify({
                text: messageInputAllVal
            })
        })

        const result = await response.json()
        console.log('Сообщение успешно отправлено, проверьте чат с ботом')

    } catch (error) {
        console.log('Ошибка', error)
    }
})

async function loadTotalUsers() {
    const totalElement = document.getElementById('totalUsers')
    try {
        const response = await fetch("http://localhost:8000/stats")
        const data = await response.json()
        const total = data.total_users
        if (data.success !== false) {
            totalElement.textContent = total
            
        }
    } catch (error) {
        console.error('Ошибка: ', error)
    }
}

window.addEventListener("load", loadTotalUsers)

setInterval(loadTotalUsers, 10000)