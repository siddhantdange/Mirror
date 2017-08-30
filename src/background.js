var mirror_api_hostname = 'textback2.herokuapp.com'
var captionsEndpoint = mirror_api_hostname + '/v1/captions'

function data_received(resp) {
  console.log(resp)
}

// Listen for a click on the camera icon. On that click, take a screenshot.
chrome.browserAction.onClicked.addListener(function() {
  chrome.tabs.captureVisibleTab(function(screenshotData) {
    $.post(captionsEndpoint, { image_data: screenshotData.toString() }, data_received);
  });
});
