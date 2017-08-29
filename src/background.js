// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// To make sure we can uniquely identify each screenshot tab, add an id as a
// query param to the url that displays the screenshot.
// Note: It's OK that this is a global variable (and not in localStorage),
// because the event page will stay open as long as any screenshot tabs are
// open.
var mirror_api_hostname = 'appvibby.herokuapp.com'
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
