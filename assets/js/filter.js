document.addEventListener("DOMContentLoaded", () => {
  const search = document.getElementById("search");
  const tagFilter = document.getElementById("tagFilter");
  const categoryFilter = document.getElementById("categoryFilter");
  const cards = document.querySelectorAll(".project-card");

  // Populate filters
  const tags = new Set();
  const categories = new Set();

  cards.forEach(card => {
    card.dataset.tags.split(" ").forEach(tag => tags.add(tag));
    categories.add(card.dataset.category);
  });

  tags.forEach(tag => {
    tagFilter.innerHTML += `<option value="${tag}">${tag}</option>`;
  });
  categories.forEach(category => {
    categoryFilter.innerHTML += `<option value="${category}">${category}</option>`;
  });

  function filterProjects() {
    const searchText = search.value.toLowerCase();
    const selectedTag = tagFilter.value;
    const selectedCategory = categoryFilter.value;

    cards.forEach(card => {
      const title = card.dataset.title;
      const tags = card.dataset.tags;
      const category = card.dataset.category;

      const matchesSearch = title.includes(searchText);
      const matchesTag = selectedTag === "all" || tags.includes(selectedTag);
      const matchesCategory = selectedCategory === "all" || category === selectedCategory;

      card.style.display = matchesSearch && matchesTag && matchesCategory ? "" : "none";
    });
  }

  search.addEventListener("input", filterProjects);
  tagFilter.addEventListener("change", filterProjects);
  categoryFilter.addEventListener("change", filterProjects);
});
