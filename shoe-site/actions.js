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
  user[0] = ["Katerine North",shopping_cart1,  39, /*shoe size*/ 20,1,2014 /*date of birth*/];
  
  user[1] = ["Kabru Lam", 40, shopping_cart2, /*shoe size*/ 20,10,2010 /*date of birth*/];
  
  user[2] = ["Pop Luca", 41,shopping_cart3, /*shoe size*/ 29,12,2003 /*date of birth*/];
  
  user[3] = ["Anastasia Kop", 38, shopping_cart4, /*shoe size*/ 12,11,2001 /*date of birth*/];
  
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
      for( let i=0; i<4; i++) {
          if(isShoppingCartEmpty(user[i])) {
              ct++;
          }
      }
  }
  
  const box=document.getElementById("box");
  
  box.innerHTML=user[0][0];

