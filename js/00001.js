//一般的な関数定義＆呼び出し
function foo(a,b){
    return a+b;
}
var result = foo(1,2)

//変数を用いた関数定義＆呼び出し
var hoge = function foo(a,b){
    return a+b;
}
var result = hoge(1,2)

//無名関数を用いた関数定義＆呼び出し
var hoge = function(a,b){
    return a+b;
}
var result = hoge(1,2)