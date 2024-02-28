# Jquery

## A bit on Syntax

### Document Ready

```javascript
$(document).ready(function () {
  // Code here
});
```

<!-- shortcut for the above -->

### Document Ready (shortcut)

```javascript
$(function () {
  // Code here
});
```

### Selectors

```javascript
$('.example');
// Selects all elements with the class "example"

$('#example');
// Selects the element with the id "example"

$('div');
// Selects all div elements

$('div.example');
// Selects all div elements with the class "example"
```

### Ajax

```javascript
$.ajax({
  type: 'GET',
  url: 'example.php',
  success: function (data) {
    // Code here
  },
});
```

### Ajax (shortcut)

```javascript
$.get('example.php', function (data) {
  // Code here
});
```

<!-- looping through a response data that is an array using foreach -->

### Looping through an array

```javascript
$.get('example.php', function (data) {
  $.each(data, function (index, value) {
    // Code here
  });
});
```

### Event Handling

```javascript
$('#update-content').click(function () {
  // AJAX request to fetch new content
  $.ajax({
    url: 'fetch_data.php', // Endpoint to fetch new data
    method: 'GET', // HTTP method
    dataType: 'html', // Expected data type
    success: function (response) {
      // Update the dynamic-content div with the fetched data
      $('#dynamic-content').html(response);
    },
    error: function (xhr, status, error) {
      // Handle error if the AJAX request fails
      console.error('Error:', error);
    },
  });
});
```

### Event Handling (on method)

```javascript
$('.example').on('click', function () {
  // Code here
});
```

### Event Handling (on method with multiple events)

```javascript
$('.example').on('click mouseover', function () {
  // Code here
});
```

<!-- api calls -->
