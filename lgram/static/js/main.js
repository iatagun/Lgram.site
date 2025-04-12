// Blog posts
const blogPosts = [
  {
    id: 1,
    title: "Building Language from Scratch",
    description:
      "How I approach AI models like raising a child — from blank slate to meaning-making entity."
  },
  {
    id: 2,
    title: "Centering Theory Meets Code",
    description:
      "Implementing discourse models that make machines sound like they’re actually paying attention."
  },
  {
    id: 3,
    title: "The Art of Linguistic Transmutation",
    description:
      "Exploring how syntax, semantics, and code can merge into human-like intelligence."
  }
];

const blogContainer = document.getElementById("blogPosts");
blogPosts.forEach((post) => {
  const article = document.createElement("article");
  article.className = "responsive-card";
  article.innerHTML = `
    <img src="https://picsum.photos/seed/code${post.id}/600/400" alt="Post illustration">
    <div class="z-10">
      <div class="category">AI & Linguistics</div>
      <h3>${post.title}</h3>
      <p>${post.description}</p>
    </div>
  `;
  article.addEventListener("click", () => alert(`You clicked on: ${post.title}`));
  blogContainer.appendChild(article);
});

// Projects
const projectData = [
  {
    id: 1,
    title: "Enhanced N-Gram Language Model",
    category: "AI & NLP",
    description:
      "A statistical model integrating Kneser-Ney smoothing, context-based selection, and coherence constraints for more human-like language generation."
  },
  {
    id: 2,
    title: "Centering Theory Transition Analyzer",
    category: "Discourse Processing",
    description:
      "A tool leveraging dependency parsing and Centering Theory to detect topic continuity and shifts in discourse-level processing."
  },
  {
    id: 3,
    title: "PsychoPy Experiment for Eye-Tracking",
    category: "Cognitive Research",
    description:
      "A visual processing experiment designed in PsychoPy with EyeLink 1000 Plus integration for cochlear implant users."
  },
  {
    id: 4,
    title: "RL-Powered Language Learning Agent",
    category: "AI Agent",
    description:
      "An interactive language agent that learns meanings, context and syntax through dynamic reinforcement learning — from scratch, like a child."
  }
];

const projectContainer = document.getElementById("projectCards");
projectData.forEach((project) => {
  const article = document.createElement("article");
  article.className = "responsive-card";
  article.innerHTML = `
    <img src="https://picsum.photos/seed/project${project.id}/600/400" alt="Project illustration">
    <div class="z-10">
      <div class="category">${project.category}</div>
      <h3>${project.title}</h3>
      <p>${project.description}</p>
    </div>
  `;
  projectContainer.appendChild(article);
});

// Alchemy input logic
const input = document.getElementById("alchemyInput");
const output = document.getElementById("alchemyConsole");

if (input && output) {
  input.addEventListener("input", (e) => {
    const val = e.target.value;
    if (val.includes("context") && val.includes("meaning")) {
      output.textContent = "🧪 Alchemy successful!";
    } else {
      output.textContent = "🔍 Needs more syntax essence.";
    }
  });
}

// Set current year in footer
document.getElementById("year").textContent = new Date().getFullYear();
