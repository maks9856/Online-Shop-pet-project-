const categoryItems = document.querySelectorAll('.category-item');
    
// Отримуємо елемент, в якому будемо змінювати текст
const categoryInfo = document.getElementById('category-info');

// Додаємо обробник події для кожного елементу
categoryItems.forEach(item => {
    item.addEventListener('mouseover', () => {
        // Встановлюємо новий текст в другому квадраті
        categoryInfo.textContent = `Вибрана категорія: ${item.getAttribute('data-name')}`;
    });
});