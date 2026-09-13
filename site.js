document.getElementById('year').textContent = new Date().getFullYear();

const quoteForm = document.getElementById('quote-form');
if (quoteForm) {
  quoteForm.addEventListener('submit', (event) => {
    event.preventDefault();
    if (!quoteForm.reportValidity()) return;
    const form = new FormData(quoteForm);
    const lines = [
      'Solicitud de cotización corporativa', '',
      `Empresa: ${form.get('company')}`,
      `Contacto: ${form.get('person')}`,
      `Teléfono: ${form.get('phone')}`,
      `Correo: ${form.get('email')}`,
      `Línea: ${form.get('line')}`,
      `Volumen aproximado: ${form.get('volume') || 'No indicado'}`,
      '', 'Detalles:', String(form.get('details') || 'No indicados'),
    ];
    const recipients = 'jestrada@divec-flexi.com,fleoutgdl@divec-flexi.com';
    const subject = encodeURIComponent(`Cotización corporativa - ${form.get('company')}`);
    const body = encodeURIComponent(lines.join('\n'));
    window.location.href = `mailto:${recipients}?subject=${subject}&body=${body}`;
  });
}

const lightbox = document.getElementById('product-lightbox');
if (lightbox) {
  const enlargedImage = lightbox.querySelector('img');
  const caption = lightbox.querySelector('p');
  const closeButton = lightbox.querySelector('.lightbox-close');

  document.querySelectorAll('[data-enlarge]').forEach((button) => {
    button.addEventListener('click', () => {
      const image = button.querySelector('img');
      const card = button.closest('.product');
      enlargedImage.src = image.currentSrc || image.src;
      enlargedImage.alt = image.alt;
      caption.textContent = card.querySelector('h3').textContent;
      lightbox.showModal();
    });
  });

  closeButton.addEventListener('click', () => lightbox.close());
  lightbox.addEventListener('click', (event) => {
    if (event.target === lightbox) lightbox.close();
  });
  lightbox.addEventListener('close', () => {
    enlargedImage.removeAttribute('src');
  });
}
