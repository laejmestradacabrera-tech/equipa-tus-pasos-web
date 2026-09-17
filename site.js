document.getElementById('year').textContent = new Date().getFullYear();

const quoteForm = document.getElementById('quote-form');
if (quoteForm) {
  const formEndpoint = 'https://script.google.com/macros/s/AKfycbyDYLcfPNrCC3xXKqoGBZOSiWzIytPtXBUVwy-sB17wbivxn2ELlpIqU6IJ-FTkNL6zVA/exec';
  const formStatus = document.getElementById('form-status');
  const submitButton = quoteForm.querySelector('button[type="submit"]');
  const requestType = document.getElementById('request_type');
  const purchaseFields = document.getElementById('purchase-fields');
  const agreementFields = document.getElementById('agreement-fields');
  const lineField = document.getElementById('line');
  const roleField = document.getElementById('role');
  const organizationTypeField = document.getElementById('organization_type');
  const cityLabel = document.getElementById('city-label');
  const cityField = document.getElementById('city');
  const otherCityContainer = document.getElementById('other-city-field');
  const otherCityField = document.getElementById('other_city');
  const detailsLabel = document.getElementById('details-label');
  const detailsField = document.getElementById('details');

  const updateConditionalFields = () => {
    const isPurchase = requestType.value === 'Cotización';
    const isAgreement = requestType.value === 'Convenio';
    purchaseFields.hidden = !isPurchase;
    agreementFields.hidden = !isAgreement;
    lineField.required = isPurchase;
    roleField.required = isAgreement;
    organizationTypeField.required = isAgreement;
    cityLabel.textContent = isPurchase ? 'Ciudad o zona de entrega *' : isAgreement ? 'Ciudad o zona del convenio *' : 'Ciudad o zona *';
    detailsLabel.textContent = isAgreement ? 'Observaciones del convenio' : 'Detalles de la solicitud';
    detailsField.placeholder = isAgreement
      ? 'Comparte alguna necesidad u observación sobre el convenio.'
      : 'Comparte modelos, tallas u otra información relevante.';
    const isOtherCity = cityField.value === 'Otra ciudad';
    otherCityContainer.hidden = !isOtherCity;
    otherCityField.required = isOtherCity;
  };

  requestType.addEventListener('change', updateConditionalFields);
  cityField.addEventListener('change', updateConditionalFields);
  updateConditionalFields();

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
      updateConditionalFields();
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

const animatedSections = document.querySelectorAll('.section');
if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  document.body.classList.add('reveal-ready');
  const sectionObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        sectionObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });
  animatedSections.forEach((section) => sectionObserver.observe(section));
}
