<template>
  <div class="quiz-container">
    <!-- Header com Pontuação e Badges -->
    <div class="status-bar">
      <p>Pontos: ⭐ {{ points }}</p>
      <p>Medalhas: {{ badges.join(" | ") || "Nenhuma" }}</p>
    </div>

    <!-- Pergunta -->
    <h2>{{ currentQuestion.question }}</h2>

    <!-- Opções -->
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

    <!-- Feedback -->
    <div v-if="selected !== null" class="feedback">
      <p v-if="isCorrect(selected)">
        Muito bem!!! Você ganhou 10 pontos. <br />
        Vamos para o próximo desafio 🎉
      </p>
      <p v-else>Boa tentativa, continue praticando!</p>
      <button @click="nextQuestion">Próximo desafio</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";

const levels = [
  [
    {
      question: "Qual é a senha mais forte?",
      options: ["Ana2024", "123456", "@na_Segura!2025"],
      answer: 2,
    },
    {
      question: "O que acontece ao escolher uma senha fraca?",
      options: ["nada muda", "você ganha pontos", "sua conta fica vulnerável"],
      answer: 2,
    },
  ],
  [
    {
      question: "Qual das opções representa melhor o que é um malware?",
      options: [
        "Um programa de segurança instalado pelo próprio usuário.",
        "Um software malicioso criado para causar danos, roubar dados ou espionar.",
        "Um sistema legítimo que atualiza automaticamente o antivírus.",
      ],
      answer: 1,
    },
    {
      question:
        "Se você está desenvolvendo um sistema de cadastro de usuários, qual medida aumenta a segurança contra ataques de phishing?",
      options: [
        "Exigir autenticação multifator no login",
        "Permitir login com senha simples para melhorar a experiência do usuário.",
        "Enviar links de redefinição de senha sem expiração.",
      ],
      answer: 0,
    },
  ],
  [
    {
      question:
        "Um tipo de malware projetado para registrar tudo o que o usuário digita no teclado é chamado de:",
      options: ["Ramsomware", "Keylogger", "Worm"],
      answer: 1,
    },
    {
      question:
        "No desenvolvimento de uma API que exige autenticação, qual prática é mais segura contra abusos relacionados a phishing?",
      options: [
        "Usar tokens de acesso de curta duração com renovação segura.",
        "Utilizar login apenas com senha para simplificar a experiência.",
        "Armazenar tokens permanentemente no navegador do usuário.",
      ],
      answer: 0,
    },
  ],
];

const currentLevel = ref(0);
const currentIndex = ref(0);
const selected = ref(null);
const correctStreak = ref(0);

const points = ref(0);
const badges = ref([]);

const currentQuestion = computed(
  () => levels[currentLevel.value][currentIndex.value]
);

function selectOption(index) {
  if (selected.value === null) {
    selected.value = index;
    if (isCorrect(index)) {
      points.value += 10; // ganha pontos
      correctStreak.value++;
    } else {
      correctStreak.value = 0; // errou, zera streak
    }
  }
}

function isCorrect(index) {
  return index === currentQuestion.value.answer;
}

function getOptionClass(index) {
  if (selected.value === null) return "";
  if (index === currentQuestion.value.answer) return "correct";
  if (index === selected.value && !isCorrect(selected.value)) return "wrong";
  return "";
}

function nextQuestion() {
  if (currentIndex.value < levels[currentLevel.value].length - 1) {
    currentIndex.value++;
    selected.value = null;
  } else {
    // fim do nível
    if (correctStreak.value === levels[currentLevel.value].length) {
      awardBadge(currentLevel.value); // dá medalha
      if (currentLevel.value < levels.length - 1) {
        alert("🎉 Você desbloqueou o próximo nível!");
        currentLevel.value++;
        currentIndex.value = 0;
        correctStreak.value = 0;
        selected.value = null;
      } else {
        alert("🏆 Parabéns! Você concluiu todos os níveis do quiz!");
      }
    } else {
      alert("Você precisa acertar todas para desbloquear o próximo nível.");
      // Reinicia o mesmo nível
      currentIndex.value = 0;
      correctStreak.value = 0;
      selected.value = null;
    }
  }
}

function awardBadge(level) {
  const badgeNames = ["🥉 Iniciante", "🥈 Intermediário", "🥇 Especialista"];
  if (!badges.value.includes(badgeNames[level])) {
    badges.value.push(badgeNames[level]);
    alert(`🏅 Você ganhou a medalha: ${badgeNames[level]}!`);
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

.status-bar {
  display: flex;
  justify-content: space-between;
  margin-bottom: 1rem;
  padding: 0.5rem;
  background: #f8f9fa;
  border-radius: 6px;
  font-weight: bold;
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
