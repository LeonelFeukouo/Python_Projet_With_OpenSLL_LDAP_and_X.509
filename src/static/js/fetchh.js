function debounce(func, timeout = 500) {
    let timer;
    return (...args) => {
        clearTimeout(() => {
            fu.apply(this, args)
        }, timeout);
    };
}

function  fetchResults(data){
    console.log(data);

}
const processChange = debounce(() => fetchResults('yes'));