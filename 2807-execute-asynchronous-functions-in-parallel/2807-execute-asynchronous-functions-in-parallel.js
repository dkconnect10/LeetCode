/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    return new Promise((resolve,reject)=>{
        let arr = Array(functions.length)
        let witingFor = functions.length
        for(let i=0; i< functions.length; i++){
            functions[i]().then((result)=>{
                arr[i]=result
                witingFor--
                if(witingFor ===0)resolve(arr)
            }).catch(reject)
        }
    })
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */