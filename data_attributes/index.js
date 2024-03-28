document.addEventListener('DOMContentLoaded', () => {

  // Returns all DOM elements with the given selector
  document.querySelectorAll('.basic-div').forEach(div => {
    
    // Event handler for mouseover
    div.addEventListener('mouseover', () => {
      console.log("Hovering");
      div.classList.add('grey-background');
    })

    // Event handler for mouseout
    div.addEventListener('mouseout', () => {
      console.log("Leaving");
      div.classList.remove('grey-background');
    })
  })


//---------------------------------------------------------


  // Add eventhandler for all div with class of 'data'
  // returning the data attribute value
  document.querySelectorAll('.data').forEach(div => {
    
    // Event listener for mouseover
    div.addEventListener('mouseover', () => {
      div.classList.add('grey-background');
      console.log(div.dataset.info);
      // console.log(div.getAttribute('data-info'));
     
    })

    // Event listener for mouseout
    div.addEventListener('mouseout', () => {
      div.classList.remove('grey-background');
  })
})


})// End DOMContentLoaded