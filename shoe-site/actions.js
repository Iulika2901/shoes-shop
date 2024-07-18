console.log("Welcome to console");
    var website="https://shoes_shop.com";
    console.log("Welcome to", website); /*comm*/
    
    
    function docWrite(variable) {
      document.write(variable);
  }

    /*-----------users-----------*/
    
    const shopping_cart1 ={'Nike ProRunner': 39,
        'Nike Ultraboost': 38.5,
        'Nike Classic': 39};
    
    const shopping_cart2 ={ 'Nike Classic': 42};
    
    const shopping_cart3 ={'Nike ProRunner': 40,
               'Nike Ultraboost': 40,
               'Nike Classic': 40};
    
    const shopping_cart4 ={'Nike ProRunner': 39,
          'Nike Ultraboost': 38.5 };
    
    let user=[];
    user[0] = ["Katerine North","123",/*name+psw*/shopping_cart1,  39, /*shoe size*/ 20,1,2014 /*date of birth*/];
    
    user[1] = ["ana","123", 40, shopping_cart2, /*shoe size*/ 20,10,2010 /*date of birth*/];
    
    user[2] = ["Pop Luca","123", 41,shopping_cart3, /*shoe size*/ 29,12,2003 /*date of birth*/];
    
    user[3] = ["Anastasia Kop","123", 38, shopping_cart4, /*shoe size*/ 12,11,2001 /*date of birth*/];
    
  let numberOfUsers = user.length; //total number of users
  
  
    function getAge(user) {
            let year = user[5];
            let age=2024 - year;
            if (age<18) console.err("under 18, need parents aprovenance");
    };
    
    function isShoppingCartEmpty(cart) {
        return Object.keys(cart).length === 0;
    }
    
    function whoHasEmpty(user){
        let ct=0;
        for( let i=0; i<numberOfUsers; i++) {
            if(isShoppingCartEmpty(user[i])) {
                ct++;
            }
        }
    }
    
    const box=document.getElementById("box");
    
    //box.innerHTML=user[0][0];
  
  /*login page*/
  
  let name="Katerine North";
  let password="123"
  function login(name, password)
  {
    let stare=[];
    stare[0]="Login excessful";
    stare[1]="Incorrect password, try again";

    let ok=1;
    for(let i=0; i<numberOfUsers; i++)
    {
      if(user[i][0]==name && user[i][1]==password)
      ok=0;
      
    }
    if(ok===1) {
      console.log("User or password incorrect");
      
       }
    else {
      console.log("Welcome", name); 
      window.location.href = "#Shopping_Cart";     
      }
      var status=stare[ok];
      document.getElementById("myText").innerHTML = status;
 
  }
  
  document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("loginForm").addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent the form from submitting
  
        let username = document.getElementById('user1').value;
        let password = document.getElementById('pass1').value;
  
        login(username, password);
    });
  });
