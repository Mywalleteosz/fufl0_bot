const mongoose = require('mongoose');
const express = require('express');
const app = express();

app.use(express.json()); // Для обработки JSON-данных

// Подключение к MongoDB
mongoose.connect('mongodb://localhost:27017/mydb', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => {
    console.log('Connected to MongoDB');
  })
  .catch((err) => {
    console.error('Failed to connect to MongoDB', err);
  });

// Определяем схему для пользователя
const userSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  age: { type: Number, required: true }
});

// Создаем модель на основе схемы
const User = mongoose.model('User', userSchema);

// Роут для добавления нового пользователя
app.post('/users', (req, res) => {
  const newUser = new User(req.body);

  newUser.save()
    .then((user) => {
      res.status(201).json(user);
    })
    .catch((err) => {
      res.status(400).json({ error: err.message });
    });
});

// Роут для получения всех пользователей
app.get('/users', (req, res) => {
  User.find()
    .then((users) => {
      res.json(users);
    })
    .catch((err) => {
      res.status(500).json({ error: err.message });
    });
});

// Запускаем сервер
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
