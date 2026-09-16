const grid = document.getElementById('catalog-grid');
const search = document.getElementById('catalog-search');
const status = document.getElementById('catalog-status');
const more = document.getElementById('catalog-more');
const dialog = document.getElementById('catalog-lightbox');
const categoryButtons = document.querySelectorAll('[data-catalog-filter]');

let catalog = [];
let filtered = [];
let visible = 12;
let activeCategory = 'all';

const normalize = (value) => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
const titleFor = (item) => item.variants.length ? item.variants.map((variant) => variant.model).join(' · ') : item.heading;

function showPage(item) {
  const image = dialog.querySelector('img');
  image.src = item.image;
  image.alt = `Página del catálogo con modelos ${titleFor(item)}`;
  dialog.querySelector('p').textContent = `Modelos ${titleFor(item)} · Consulta precio y disponibilidad`;
  dialog.showModal();
}

function render() {
  grid.replaceChildren();
  filtered.slice(0, visible).forEach((item) => {
    const card = document.createElement('article');
    card.className = 'catalog-card';

    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'catalog-page-button';
    button.setAttribute('aria-label', `Ampliar modelos ${titleFor(item)}`);

    const image = document.createElement('img');
    image.src = item.image;
    image.alt = `Modelos ${titleFor(item)} del catálogo Flexi`;
    image.loading = 'lazy';
    button.append(image);
    button.addEventListener('click', () => showPage(item));

    const heading = document.createElement('h3');
    heading.textContent = item.name || `Modelos ${titleFor(item)}`;

    const models = document.createElement('p');
    models.className = 'catalog-models';
    models.textContent = item.variants.length
      ? item.variants.map((variant) => `${variant.model} ${variant.color}`).join(' · ')
      : 'Información de tecnologías y atributos Flexi';

    const link = document.createElement('a');
    link.className = 'text-link';
    link.href = 'index.html#contacto';
    link.textContent = 'Consultar precio →';

    card.append(button, heading, models, link);
    grid.append(card);
  });

  const categoryLabel = activeCategory === 'all' ? 'en todo el catálogo' : `en ${activeCategory}`;
  status.textContent = filtered.length === 1
    ? `1 página encontrada ${categoryLabel}.`
    : `${filtered.length} páginas encontradas ${categoryLabel}.`;
  more.hidden = visible >= filtered.length;
}

function filterCatalog() {
  const query = normalize(search.value.trim());
  filtered = catalog.filter((item) => {
    const matchesCategory = activeCategory === 'all' || item.category === activeCategory;
    const matchesSearch = !query || normalize(item.search).includes(query);
    return matchesCategory && matchesSearch;
  });
  visible = 12;
  render();
}

categoryButtons.forEach((button) => {
  button.addEventListener('click', () => {
    activeCategory = button.dataset.catalogFilter;
    categoryButtons.forEach((candidate) => {
      const isActive = candidate === button;
      candidate.classList.toggle('active', isActive);
      candidate.setAttribute('aria-pressed', String(isActive));
    });
    filterCatalog();
  });
});

more.addEventListener('click', () => {
  visible += 12;
  render();
});
search.addEventListener('input', filterCatalog);
dialog.querySelector('.lightbox-close').addEventListener('click', () => dialog.close());
dialog.addEventListener('click', (event) => {
  if (event.target === dialog) dialog.close();
});

fetch('catalogo.json')
  .then((response) => {
    if (!response.ok) throw new Error();
    return response.json();
  })
  .then((data) => {
    catalog = data;
    filterCatalog();
  })
  .catch(() => {
    status.textContent = 'No fue posible cargar el catálogo. Intenta nuevamente.';
  });
