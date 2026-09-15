document.getElementById('year').textContent = new Date().getFullYear();

const quoteForm = document.getElementById('quote-form');
if (quoteForm) {
  const formEndpoint = 'https://script.google.com/macros/s/AKfycbyDYLcfPNrCC3xXKqoGBZOSiWzIytPtXBUVwy-sB17wbivxn2ELlpIqU6IJ-FTkNL6zVA/exec';
  const formStatus = document.getElementById('form-status');
  const submitButton = quoteForm.querySelector('button[type="submit"]');

  quoteForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    if (!quoteForm.reportValidity()) return;
    formStatus.className = 'form-status';
    formStatus.textContent = 'Enviando tu solicitud…';
    submitButton.disabled = true;

    const form = new FormData(quoteForm);
    form.set('source', window.location.href);

    try {
      await fetch(formEndpoint, { method: 'POST', body: form, mode: 'no-cors' });
      quoteForm.reset();
      formStatus.className = 'form-status success';
      formStatus.textContent = 'Solicitud enviada. Nuestro equipo se pondrá en contacto contigo.';
    } catch (error) {
      formStatus.className = 'form-status error';
      formStatus.textContent = 'No fue posible enviar la solicitud. Escríbenos por WhatsApp o intenta nuevamente.';
    } finally {
      submitButton.disabled = false;
    }
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
