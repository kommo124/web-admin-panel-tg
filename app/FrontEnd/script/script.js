const messageInput = document.getElementById('messageInput')
const sendBtn = document.getElementById('sendBtn')
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