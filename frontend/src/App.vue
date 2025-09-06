<template>
  <div class="quiz-container">
    <h2>{{ currentQuestion.question }}</h2>
    
    <ul>
      <li 
        v-for="(option, index) in currentQuestion.options" 
        :key="index"
        :class="getOptionClass(index)"
        @click="selectOption(index)"
      >
        {{ option }}
        <span v-if="selected === index">
          <template v-if="isCorrect(index)">✅</template>
          <template v-else>❌</template>
        </span>
      </li>
    </ul>
    
    <div v-if="selected !== null" class="feedback">
      <p v-if="isCorrect(selected)">Muito bem!!! Você ganhou 10 estrelas. <br> Vamos para o próximo desafio 🎉</p>
      <p v-else>Boa tentativa, continue praticando!</p>
      <button @click="nextQuestion">Próximo desafio</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const questions = [
  {
    question: 'Qual é a senha mais forte?',
    options: ['Ana2024', '123456', '@na_Segura!2025'],
    answer: 2
  },
  {
    question: 'O que acontece ao escolher uma senha fraca?',
    options: ['nada muda', 'você ganha pontos', 'sua conta fica vulnerável'],
    answer: 2
  }
]

const currentIndex = ref(0)
const selected = ref(null)

const currentQuestion = computed(() => questions[currentIndex.value])

function selectOption(index) {
  if (selected.value === null) {
    selected.value = index
  }
}

function isCorrect(index) {
  return index === currentQuestion.value.answer
}

function getOptionClass(index) {
  if (selected.value === null) return ''
  if (index === currentQuestion.value.answer) return 'correct'
  if (index === selected.value && !isCorrect(selected.value)) return 'wrong'
  return ''
}

function nextQuestion() {
  if (currentIndex.value < questions.length - 1) {
    currentIndex.value++
    selected.value = null
  } else {
    alert('Parabéns! Você concluiu o quiz.')
  }
}
</script>

<style scoped>
.quiz-container {
  max-width: 500px;
  margin: 2rem auto;
  font-family: Arial, sans-serif;
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 6px;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  padding: 10px;
  border: 1px solid #ddd;
  margin-bottom: 8px;
  cursor: pointer;
  border-radius: 4px;
  user-select: none;
  transition: background-color 0.3s ease;
}

li.correct {
  background-color: #d4edda;
  border-color: #28a745;
  color: #155724;
}

li.wrong {
  background-color: #f8d7da;
  border-color: #dc3545;
  color: #721c24;
}

.feedback {
  margin-top: 20px;
}

button {
  cursor: pointer;
  padding: 8px 16px;
  margin-top: 10px;
  background-color: #007bff;
  border: none;
  color: white;
  border-radius: 4px;
  font-size: 1rem;
}

button:hover {
  background-color: #0056b3;
}
</style>
