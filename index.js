const express = require('express');
const app = express();

// Указываем, что будем использовать EJS
app.set('view engine', 'ejs');

// Рендерим страницу с использованием EJS
app.get('/', (req, res) => {
  res.render('index', { title: 'Home Page' });
});

// Статическая папка для файлов (например, CSS, изображения)
app.use(express.static('public'));

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
