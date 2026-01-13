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

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // Get the mails for the mailbox and user
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
      // loop through emails and create a div for each
      emails.forEach(email => {
        // create div for each email
        const now = document.createElement('div');
        row.className = 'email-row';
        row.style.border = '1px solid #cc';
        row.style.padding = '10px';
        row.style.cursor = 'pointer';
        // gray background if read
        if (email.read) {
          row.style.backgrounColor = '#f0f0f0';
        } else {
          row.style.backgrounColor = 'white';
          row.style.fontWeight = 'bold';
        }
        row.innerHTML = `
          <span>${email.sender}</span>
          <span style="margin-left: 20px;">${email.subject}</span>
          <span style="float: right;">${email.timestamp}</span>
        `;

        row.addEventListener('click', () => {
          console.log(`Opening email ID: ${email.id}`);
          view_email(email.id); // your email detail function
        });

        document.querySelector('#emails-view').append(row);
      });
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
