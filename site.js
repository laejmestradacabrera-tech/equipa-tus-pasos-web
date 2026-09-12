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
