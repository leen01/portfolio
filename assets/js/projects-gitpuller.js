fetch('https://api.github.com/users/leen01/repos', {
  headers: {
    Accept: 'application/vnd.github.mercy-preview+json'
  }
})
  .then(res => res.json())
  .then(repos => {
    const container = document.querySelector('.project-grid');
    const portfolioRepos = repos.filter(repo =>
      repo.topics && repo.topics.includes('portfolio')
    );

    // Function to capitalize each word
    const capitalizeWords = (str) => {
      return str.replace(/\b\w/g, char => char.toUpperCase());
    };

    portfolioRepos.forEach(repo => {
      const card = document.createElement('div');
      card.classList.add('project-card');

      // --- Automatic Image ---
      const imageName = repo.name.toLowerCase().replace(/ /g, '-').replace(/_/g, '-') + '.png';
      const imageUrl = `/assets/img/projects/${repo.name}.png` || repo.homepage;

      card.innerHTML = `
        <div class="card-image" style="background-image: url('${imageUrl}');">
          <div class="card-overlay">
            <p>${repo.description || "No description available."}</p>
          </div>
        </div>
        <div class="card-body">
          <h3>${capitalizeWords(repo.name.replace(/-/g, ' ').replace(/_/g, ' '))}</h3>
          <a href="${repo.html_url}" target="_blank" class="view-link">View Project</a>
        </div>
      `;
      container.appendChild(card);
    });
  });
