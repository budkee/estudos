const funcs = [] 

for (var i = 0; i< 10 ; i++) {
 
  funcs.push (function() {
    console.log(i)
    
  })
}

funcs[2]() // i = 2
funcs[8]() // i = 8

// Conceito de closure: uma função saberá onde foi definida.