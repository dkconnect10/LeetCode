/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    
    let value = init
     obj = {
        increment:()=>{
            return ++value
        },
        decrement:()=>{
            return --value
        },
        reset:()=>{
            value = init
            return value
        }


     }
     return obj
    
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */