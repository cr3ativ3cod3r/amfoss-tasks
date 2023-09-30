var number=prompt("Enter a number: ");
var List=[2];
for (let i = 3; i <= number; i++){
    var a=0
    for (let j = 0;j < List.length; j++){
        if (i%List[j]!=0){
            a++
        }
    }
    if (List.length==a){
        List.push(i)

    }
}
if (number>=2){
    console.log(List)}
