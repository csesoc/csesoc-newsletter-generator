chrome.action.onClicked.addListener(() => {
  console.log("Extension icon clicked!");
  const indexURL = chrome.runtime.getURL("index.html");
  console.log("Opening URL:", indexURL);
  
  // Use the promise-based API for creating tabs
  chrome.tabs.create({ url: indexURL })
    .then(tab => {
      console.log("Tab created successfully:", tab.id);
    })
    .catch(error => {
      console.error("Error creating tab:", error);
    });
});