document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // Submitten
  document.querySelector('#compose-form').addEventListener('submit', send_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {

  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#email-detail-view').style.display = 'none';



  // Show the mailbox name
  const container = document.querySelector('#emails-view');
  container.innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // Get the mails for the mailbox and user
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {

      // loop through emails and create a div for each
      emails.forEach(email => {
        console.log(email.id, email.read);

        // create div for each email
        const row = document.createElement('div');
        row.className = 'email-row';
        row.style.border = '1px solid #ccc';
        row.style.padding = '10px';
        row.style.cursor = 'pointer';

        // gray background if read
        if (email.read) {
          row.style.backgroundColor = 'gray';
        } else {
          row.style.backgroundColor = 'white';
          row.style.fontWeight = 'bold';
        }
        row.innerHTML = `
          <span>${email.sender}</span>
          <span style="margin-left: 20px;">${email.subject}</span>
          <span style="float: right;">${email.timestamp}</span>
        `;

        row.addEventListener('click', () => {
          row.style.backgroundColor = 'gray';
          row.style.fontWeight = 'normal';
          view_email(email.id); // your email detail function
        });

        document.querySelector('#emails-view').append(row);
      });
    });
  }

function view_email(email_id) {

    // Mostrar vista individual
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'none';
    document.querySelector('#email-detail-view').style.display = 'block';


    fetch(`/emails/${email_id}`)
      .then(response => response.json())
      .then(email => {

        const detail = document.querySelector('#email-detail-view');

        // control of archive button
        const archive = document.querySelector('#archive-btn');
        if (mailbox === 'sent') {
          archive.style.display = 'none';
        } else {
          archive.style.display = 'block';
        }

        detail.innerHTML = `
          <p><strong>From:</strong> ${email.sender}</p>
          <p><strong>To:</strong> ${email.recipients}</p>
          <p><strong>Subject:</strong> ${email.subject}</p>
          <p><strong>Timestamp:</strong> ${email.timestamp}</p>
          <hr>
          <p>${email.body}</p>
          <button class="btn btn-sm btn-outline-primary" id="archive-btn">${email.archived ? 'Unarchive' : 'Archive'}</button>
        `;

        // Marcar como leído
        fetch(`/emails/${email_id}`, {
          method: 'PUT',
          body: JSON.stringify({ read: true })
        });
        // logica del boton archive
        document.querySelector('#archive-btn').onclick = () => {
          fetch(`/emails/${email_id}`, {
            method: 'PUT',
            body: JSON.stringify({
              archived: !email.archived
            })
          }).then(() => {
            fetch(`/emails/${email_id}`)
            .then(response => response.json())
            .then(updated_email => {
              document.querySelector('#archive-btn').innerText =
              updated_email.archived ? 'Unarchive' : 'Archive';
            });
          });
        };
      });
  }



function send_email (event) {
  event.preventDefault();

  //Store Fields
  const recipients = document.querySelector('#compose-recipients').value;
  const subject = document.querySelector('#compose-subject').value;
  const body = document.querySelector('#compose-body').value;


  // Send data to backend
  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
      recipients: recipients,
      subject: subject,
      body: body,
    })

  })
  .then(response => response.json())
  .then(result => {
    // Print result
    console.log(result);
    load_mailbox('sent');
  });
}
