const noteForm = document.getElementById('note-form');
const noteList = document.getElementById('note-list');
let editingNoteId = null;

// Получить все заметки
async function fetchNotes() {
    const response = await fetch('/notes/');
    const notes = await response.json();
    noteList.innerHTML = '';
    notes.forEach(note => {
        const noteItem = document.createElement('div');
        noteItem.className = 'border p-4 mt-2 rounded-lg shadow hover:shadow-lg transition';
        noteItem.innerHTML = `
            <h2 class="font-bold text-3xl text-white transition duration-200 break-words mb-4">${note.title}</h2> <!-- Яркий заголовок -->
            <hr></hr>
            <p class="text-white font-bold break-words mt-4">${note.text}</p> <!-- Темный текст заметки -->
            <div class="mt-4 flex space-x-2 ">
                <button class="bg-yellow-500 text-white font-bold rounded-lg p-2 hover:bg-yellow-400 transition duration-200 transform hover:scale-105" onclick="editNote(${note.id}, '${note.title}', '${note.text}')">Редактировать</button>
                <button class="bg-red-600 text-white font-bold rounded-lg p-2 hover:bg-red-500 transition duration-200 transform hover:scale-105" onclick="deleteNote(${note.id})">Удалить</button>
            </div>
        `;
        noteList.appendChild(noteItem);
    });
}

// Добавить заметку
noteForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    const title = document.getElementById('note-title').value;
    const text = document.getElementById('note-text').value;

    if (editingNoteId) {
        // Если редактируем, отправляем PUT-запрос
        await fetch(`/notes/${editingNoteId}/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ title, text }),
        });
        editingNoteId = null; // Сбрасываем ID редактируемой заметки
    } else {
        // Если добавляем новую заметку, отправляем POST-запрос
        await fetch('/notes/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ title, text }),
        });
    }

    fetchNotes(); // Обновить список заметок
    noteForm.reset(); // Очистить форму
});

// Функция редактирования заметки
function editNote(id, title, text) {
    editingNoteId = id; // Сохраняем ID редактируемой заметки
    document.getElementById('note-title').value = title; // Заполняем поля формы
    document.getElementById('note-text').value = text;
}

// Функция удаления заметки
async function deleteNote(id) {
    await fetch(`/notes/${id}/`, {
        method: 'DELETE',
    });
    fetchNotes(); // Обновить список заметок
}

fetchNotes(); // Получить заметки при загрузке
