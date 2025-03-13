document.addEventListener("DOMContentLoaded", function () {
    // Get containers
    const eventsContainer = document.getElementById("events-container");
    const articlesContainer = document.getElementById("articles-container");
    const opportunitiesContainer = document.getElementById(
      "opportunities-container"
    );
    const downloadLink = document.getElementById("download-link");

    // Add button event listeners
    document
      .getElementById("add-event-btn")
      .addEventListener("click", addEventForm);
    document
      .getElementById("add-article-btn")
      .addEventListener("click", addArticleForm);
    document
      .getElementById("add-opportunity-btn")
      .addEventListener("click", addOpportunityForm);
    document
      .getElementById("generate-btn")
      .addEventListener("click", generateNewsletter);

    function createFormCard() {
      const formCard = document.createElement("div");
      formCard.className = "form-card";
      return formCard;
    }

    function createFormGroup(
      labelText,
      inputType = "text",
      isTextArea = false
    ) {
      const formGroup = document.createElement("div");
      formGroup.className = "form-group";

      const label = document.createElement("label");
      label.textContent = labelText;
      formGroup.appendChild(label);

      let input;
      if (isTextArea) {
        input = document.createElement("textarea");
      } else {
        input = document.createElement("input");
        input.type = inputType;
      }

      formGroup.appendChild(input);
      return { formGroup, input };
    }

    function createDeleteButton(container, card) {
      const deleteBtn = document.createElement("button");
      deleteBtn.className = "delete-btn";
      deleteBtn.textContent = "Delete";
      deleteBtn.addEventListener("click", function () {
        container.removeChild(card);
      });
      return deleteBtn;
    }

    function addEventForm() {
      const card = createFormCard();

      // Create form fields
      const { formGroup: urlGroup, input: urlInput } =
        createFormGroup("Event URL:");
      urlInput.className = "event-url";
      card.appendChild(urlGroup);

      const { formGroup: titleGroup, input: titleInput } =
        createFormGroup("Event Title:");
      titleInput.className = "event-title";
      card.appendChild(titleGroup);

      const { formGroup: timeGroup, input: timeInput } =
        createFormGroup("Event Time:");
      timeInput.className = "event-time";
      card.appendChild(timeGroup);

      const { formGroup: locationGroup, input: locationInput } =
        createFormGroup("Event Location:");
      locationInput.className = "event-location";
      card.appendChild(locationGroup);

      const { formGroup: imgGroup, input: imgInput } =
        createFormGroup("Image URL:");
      imgInput.className = "event-img";
      card.appendChild(imgGroup);

      const { formGroup: descGroup, input: descInput } = createFormGroup(
        "Description:",
        "text",
        true
      );
      descInput.className = "event-desc";
      card.appendChild(descGroup);

      const deleteBtn = createDeleteButton(eventsContainer, card);
      card.appendChild(deleteBtn);

      eventsContainer.appendChild(card);
    }

    function addArticleForm() {
      const card = createFormCard();

      // Create form fields
      const { formGroup: urlGroup, input: urlInput } =
        createFormGroup("Article URL:");
      urlInput.className = "article-url";
      card.appendChild(urlGroup);

      const { formGroup: titleGroup, input: titleInput } =
        createFormGroup("Article Title:");
      titleInput.className = "article-title";
      card.appendChild(titleGroup);

      const { formGroup: imgGroup, input: imgInput } =
        createFormGroup("Image URL:");
      imgInput.className = "article-img";
      card.appendChild(imgGroup);

      const { formGroup: descGroup, input: descInput } = createFormGroup(
        "Description:",
        "text",
        true
      );
      descInput.className = "article-desc";
      card.appendChild(descGroup);

      const deleteBtn = createDeleteButton(articlesContainer, card);
      card.appendChild(deleteBtn);

      articlesContainer.appendChild(card);
    }

    function addOpportunityForm() {
      const card = createFormCard();

      // Create form fields
      const { formGroup: titleGroup, input: titleInput } =
        createFormGroup("Opportunity Title:");
      titleInput.className = "opportunity-title";
      card.appendChild(titleGroup);

      const { formGroup: descGroup, input: descInput } = createFormGroup(
        "Description:",
        "text",
        true
      );
      descInput.className = "opportunity-desc";
      card.appendChild(descGroup);

      const deleteBtn = createDeleteButton(opportunitiesContainer, card);
      card.appendChild(deleteBtn);

      opportunitiesContainer.appendChild(card);
    }

    function generateNewsletterHTML(events, articles, opportunities) {
      // Start with the basic HTML structure
      let html = `<!DOCTYPE html>
      <html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml">
      <head>
          <title>soc-announce</title>
          <meta http-equiv="X-UA-Compatible" content="IE=edge">
          <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <link href="https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700" rel="stylesheet" type="text/css">
          <link href="https://fonts.googleapis.com/css2?family=Ubuntu+Mono&display=swap" rel="stylesheet" type="text/css">
      </head>
      <body>
          <table id="bodyTable" width="100%">
              <tr>
                  <td align="center">
                      <table id="emailContainer" width="800" cellpadding="50" cellspacing="0" style="background: #f0f0f0;">
                          <tr>
                              <td>
                                  <table id="emailContent" width="700" cellpadding="0" cellspacing="0" style="background: white;">
                                      <thead>
                                          <tr>
                                              <td>
                                                  <table id="emailHeader" width="100%" cellpadding="0" cellspacing="0">
                                                      <tr>
                                                          <td>
                                                              <!-- Header -->
                                                              <h1 style="color: #1051ea; font-family: Helvetica, Arial, sans-serif; text-align: center; margin: 20px 0;">CSESoc Newsletter</h1>
                                                              <hr style="border: none; border-top: 2px solid #1051ea; width: 80%; margin: 10px auto;">
                                                          </td>
                                                      </tr>
                                                  </table>
                                              </td>
                                          </tr>
                                      </thead>
                                      <tbody>
                                          <tr>
                                              <td>
                                                  <table id="emailBody" width="100%" cellpadding="0" cellspacing="0">`;

      // Add events section if we have events
      if (events.length > 0) {
        html += `
                                                      <tr>
                                                          <td>
                                                              <table id="upcomingEvents" width="100%" cellpadding="0" cellspacing="0">
                                                                  <tr>
                                                                      <td>
                                                                          <table cellpadding="10">
                                                                              <tr>
                                                                                  <th colspan="2" style="text-align: center;">
                                                                                      <table cellpadding="20" style="margin-left: auto; margin-right: auto;">
                                                                                          <tr>
                                                                                              <td>
                                                                                                  <table>
                                                                                                      <tr>
                                                                                                          <td>
                                                                                                              <h2 style="font-family: Helvetica, Arial, sans-serif; font-weight: bold; font-size: 24px; text-transform: uppercase; text-align: center; line-height: 2; border-bottom: 5px solid #1051ea; margin-block-start: 0; margin-block-end: 0;">Events</h2>
                                                                                                          </td>
                                                                                                      </tr>
                                                                                                  </table>
                                                                                              </td>
                                                                                          </tr>
                                                                                      </table>
                                                                                  </th>
                                                                              </tr>`;

        // Add each event - following format in events.py
        events.forEach((event, index) => {
          const eventId = event.title
            .toLowerCase()
            .replace(/[^a-z0-9]+/g, "-");

          html += `
                                                                              <tr>
                                                                                  <td colspan="2">
                                                                                      <p style="border-top: 3px dashed #f0f0f0; width: 100%;"></p>
                                                                                  </td>
                                                                              </tr>
                                                                              <tr id="event-${eventId}">
                                                                                  <td width="45%" style="vertical-align: top">
                                                                                      <table style="width: 100%">
                                                                                          <tr>
                                                                                              <td>
                                                                                                  <a href="${event.url}" target="_blank">
                                                                                                      <img src="${event.img}" width="100%" alt="Cover photo for ${event.title}" style="border-radius: 8px;">
                                                                                                  </a>
                                                                                              </td>
                                                                                          </tr>
                                                                                          <tr>
                                                                                              <td>
                                                                                                  <table cellpadding="5" style="font-family: Helvetica, Arial, sans-serif; color: #666; font-size: 14px;">
                                                                                                      <tr>
                                                                                                          <td>📆</td>
                                                                                                          <td>${event.time}</td>
                                                                                                      </tr>`;

          if (event.location) {
            html += `
                                                                                                      <tr>
                                                                                                          <td>📍</td>
                                                                                                          <td>${event.location}</td>
                                                                                                      </tr>`;
          }

          html += `
                                                                                                  </table>
                                                                                              </td>
                                                                                          </tr>
                                                                                      </table>
                                                                                  </td>
                                                                                  <td width="55%" style="vertical-align: top">
                                                                                      <table style="width: 100%">
                                                                                          <tr>
                                                                                              <td>
                                                                                                  <h3 style="color: #1051ea; font-weight: bold; font-size: 18px; font-family: Helvetica, Arial, sans-serif; margin-top: 0;">${event.title}</h3>
                                                                                              </td>
                                                                                          </tr>
                                                                                          <tr>
                                                                                              <td>
                                                                                                  <div style="margin: 0; font-family: Helvetica, Arial, sans-serif; color: #444; line-height: 1.5;">
                                                                                                      ${event.description}
                                                                                                  </div>
                                                                                              </td>
                                                                                          </tr>
                                                                                          <tr>
                                                                                              <td>
                                                                                                  <a href="${event.url}" target="_blank" style="display: inline-block; background-color: #1051ea; color: white; text-decoration: none; padding: 10px 20px; border-radius: 5px; margin-top: 10px; font-family: Helvetica, Arial, sans-serif;">See more</a>
                                                                                              </td>
                                                                                          </tr>
                                                                                      </table>
                                                                                  </td>
                                                                              </tr>`;
        });

        html += `
                                                                          </table>
                                                                      </td>
                                                                  </tr>
                                                              </table>
                                                          </td>
                                                      </tr>`;
      }

      // Add articles section if we have articles
      if (articles.length > 0) {
        html += `
                                                      <tr>
                                                          <td>
                                                              <table id="mediaArticles" width="100%" cellpadding="0" cellspacing="0">
                                                                  <tr>
                                                                      <td>
                                                                          <table cellpadding="10">
                                                                              <tr>
                                                                                  <th colspan="2" style="text-align: center;">
                                                                                      <table cellpadding="20" style="margin-left: auto; margin-right: auto;">
                                                                                          <tr>
                                                                                              <td>
                                                                                                  <table>
                                                                                                      <tr>
                                                                                                          <td>
                                                                                                              <h2 style="font-family: Helvetica, Arial, sans-serif; font-weight: bold; font-size: 24px; text-transform: uppercase; text-align: center; line-height: 2; border-bottom: 5px solid #1051ea; margin-block-start: 0; margin-block-end: 0;">Media</h2>
                                                                                                          </td>
                                                                                                      </tr>
                                                                                                  </table>
                                                                                              </td>
                                                                                          </tr>
                                                                                      </table>
                                                                                  </th>
                                                                              </tr>`;

        // Add each article - following format in articles.py
        articles.forEach((article, index) => {
          const articleId = article.title
            .toLowerCase()
            .replace(/[^a-z0-9]+/g, "-");

          html += `
                                                                              <tr>
                                                                                  <td colspan="2">
                                                                                      <p style="border-top: 3px dashed #f0f0f0; width: 100%;"></p>
                                                                                  </td>
                                                                              </tr>
                                                                              <tr id="article-${articleId}">
                                                                                  <td width="45%" style="vertical-align: top">
                                                                                      <table style="width: 100%">
                                                                                          <tr>
                                                                                              <td>
                                                                                                  <a href="${article.url}" target="_blank">
                                                                                                      <img src="${article.img}" width="100%" alt="Cover photo for ${article.title}" style="border-radius: 8px;">
                                                                                                  </a>
                                                                                              </td>
                                                                                          </tr>
                                                                                      </table>
                                                                                  </td>
                                                                                  <td width="55%" style="vertical-align: top">
                                                                                      <table style="width: 100%">
                                                                                          <tr>
                                                                                              <td>
                                                                                                  <h3 style="color: #1051ea; font-weight: bold; font-size: 18px; font-family: Helvetica, Arial, sans-serif; margin-top: 0;">${article.title}</h3>
                                                                                              </td>
                                                                                          </tr>
                                                                                          <tr>
                                                                                              <td>
                                                                                                  <div style="margin: 0; font-family: Helvetica, Arial, sans-serif; color: #444; line-height: 1.5;">
                                                                                                      ${article.description}
                                                                                                  </div>
                                                                                              </td>
                                                                                          </tr>
                                                                                          <tr>
                                                                                              <td>
                                                                                                  <a href="${article.url}" target="_blank" style="display: inline-block; background-color: #1051ea; color: white; text-decoration: none; padding: 10px 20px; border-radius: 5px; margin-top: 10px; font-family: Helvetica, Arial, sans-serif;">Read more</a>
                                                                                              </td>
                                                                                          </tr>
                                                                                      </table>
                                                                                  </td>
                                                                              </tr>`;
        });

        html += `
                                                                          </table>
                                                                      </td>
                                                                  </tr>
                                                              </table>
                                                          </td>
                                                      </tr>`;
      }

      // Add opportunities section if we have opportunities
      if (opportunities.length > 0) {
        html += `
                                                      <tr>
                                                          <td>
                                                              <table id="opportunities" width="100%" cellpadding="0" cellspacing="0">
                                                                  <tr>
                                                                      <td>
                                                                          <table cellspacing="0" cellpadding="0">
                                                                              <tr>
                                                                                  <th colspan="2" style="text-align: center;">
                                                                                      <table cellpadding="20" style="margin-left: auto; margin-right: auto;">
                                                                                          <tr>
                                                                                              <td>
                                                                                                  <table>
                                                                                                      <tr>
                                                                                                          <td>
                                                                                                              <h2 style="font-family: Helvetica, Arial, sans-serif; font-weight: bold; font-size: 24px; text-transform: uppercase; text-align: center; line-height: 2; border-bottom: 5px solid #1051ea; margin-block-start: 0; margin-block-end: 0;">Opportunities</h2>
                                                                                                          </td>
                                                                                                      </tr>
                                                                                                  </table>
                                                                                              </td>
                                                                                          </tr>
                                                                                      </table>
                                                                                  </th>
                                                                              </tr>
                                                                              <tr>
                                                                                  <td colspan="2">
                                                                                      <p style="border-top: 3px dashed #f0f0f0; width: 100%;"></p>
                                                                                  </td>
                                                                              </tr>
                                                                              <tr>
                                                                                  <td>
                                                                                      <table cellpadding="20">`;

        // Add each opportunity - following format in opportunities.py
        opportunities.forEach((opportunity, index) => {
          const opportunityId = opportunity.title
            .toLowerCase()
            .replace(/[^a-z0-9]+/g, "-");

          html += `
                                                                                          <tr id="opportunity-${opportunityId}">
                                                                                              <td>
                                                                                                  <table cellpadding="10" style="border-left: 5px solid #1051ea;">
                                                                                                      <tr>
                                                                                                          <td>
                                                                                                              <table>
                                                                                                                  <tr>
                                                                                                                      <td>
                                                                                                                          <h3 style="color: #1051ea; font-weight: bold; font-size: 18px; font-family: Helvetica, Arial, sans-serif; margin-top: 0;">${opportunity.title}</h3>
                                                                                                                      </td>
                                                                                                                  </tr>
                                                                                                                  <tr>
                                                                                                                      <td>
                                                                                                                          <div style="margin: 0; font-family: Helvetica, Arial, sans-serif; color: #444; line-height: 1.5;">
                                                                                                                              ${opportunity.description}
                                                                                                                          </div>
                                                                                                                      </td>
                                                                                                                  </tr>
                                                                                                              </table>
                                                                                                          </td>
                                                                                                      </tr>
                                                                                                  </table>
                                                                                              </td>
                                                                                          </tr>`;
        });

        html += `
                                                                                      </table>
                                                                                  </td>
                                                                              </tr>
                                                                          </table>
                                                                      </td>
                                                                  </tr>
                                                              </table>
                                                          </td>
                                                      </tr>`;
      }

      // Complete the HTML structure with footer
      html += `
                                                  </table>
                                              </td>
                                          </tr>
                                      </tbody>
                                      <tfoot>
                                          <tr>
                                              <td>
                                                  <table id="emailFooter" width="100%" cellpadding="0" cellspacing="0">
                                                      <tr>
                                                          <td style="padding: 20px; text-align: center;">
                                                              <p style="margin: 0; font-family: Helvetica, Arial, sans-serif; color: #666; font-size: 12px;">© CSESoc UNSW</p>
                                                              <p style="margin: 5px 0 0; font-family: Helvetica, Arial, sans-serif; color: #666; font-size: 12px;">
                                                                  <a href="https://www.csesoc.unsw.edu.au/" style="color: #1051ea; text-decoration: none;">www.csesoc.unsw.edu.au</a>
                                                              </p>
                                                          </td>
                                                      </tr>
                                                  </table>
                                              </td>
                                          </tr>
                                      </tfoot>
                                  </table>
                              </td>
                          </tr>
                      </table>
                  </td>
              </tr>
          </table>
      </body>
      </html>`;

      return html;
    }

    function generateNewsletter() {
      try {
        // Show loading state
        downloadLink.innerHTML = `<p>Generating newsletter...</p>`;
        downloadLink.style.display = "block";

        // Collect events data
        const eventForms = eventsContainer.querySelectorAll(".form-card");
        const events = Array.from(eventForms).map((form) => {
          return {
            url: form.querySelector(".event-url").value,
            title: form.querySelector(".event-title").value,
            description: form
              .querySelector(".event-desc")
              .value.replace(/\n/g, "<br />"),
            time: form.querySelector(".event-time").value,
            location: form.querySelector(".event-location").value,
            img: form.querySelector(".event-img").value,
          };
        });

        // Collect articles data
        const articleForms =
          articlesContainer.querySelectorAll(".form-card");
        const articles = Array.from(articleForms).map((form) => {
          return {
            url: form.querySelector(".article-url").value,
            title: form.querySelector(".article-title").value,
            description: form
              .querySelector(".article-desc")
              .value.replace(/\n/g, "<br />"),
            img: form.querySelector(".article-img").value,
          };
        });

        // Collect opportunities data
        const opportunityForms =
          opportunitiesContainer.querySelectorAll(".form-card");
        const opportunities = Array.from(opportunityForms).map((form) => {
          return {
            title: form.querySelector(".opportunity-title").value,
            description: form
              .querySelector(".opportunity-desc")
              .value.replace(/\n/g, "<br />"),
          };
        });

        // Generate preview with local data
        const previewContainer =
          document.getElementById("preview-container");
        const previewElement =
          document.getElementById("newsletter-preview");
        const localHtml = generateNewsletterHTML(
          events,
          articles,
          opportunities
        );
        previewElement.innerHTML = localHtml;
        previewContainer.style.display = "block";

        // Send the data to backend
        fetch("http://localhost:5000/generate", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            events: events,
            articles: articles,
            opportunities: opportunities,
          }),
        })
          .then((response) => response.json())
          .then((data) => {
            if (data.success) {
              // Update download link to actually be a download button for the content
              const htmlContent = data.html;
              const blob = new Blob([htmlContent], { type: "text/html" });
              const url = URL.createObjectURL(blob);

              downloadLink.innerHTML = `
                <a href="${url}" download="newsletter.html">Click Here to Download Newsletter HTML</a>
              `;
              downloadLink.style.display = "block";

              // Update preview with server-generated HTML if it differs
              previewElement.innerHTML = htmlContent;
            } else {
              alert("Error: " + data.error);
            }
          })
          .catch((error) => {
            console.error("Error:", error);
            alert("Error: " + error);
          });
      } catch (error) {
        alert("Error generating newsletter: " + error.message);
      }
    }
  });