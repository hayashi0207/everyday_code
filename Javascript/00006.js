//即時関数の書き方
//  const 〇〇　＝　(アロー関数)();
//即時関数は定義するだけで即座に処理が実行される。つまり呼び出しを必要としない。
const headerModule = (()=>{
    //初期化処理
    let counter=0
    
    return{
        //メソッド化
        countUp:()=>{
            counter +=1
            console.log("現在のカウンタ" + counter)
        },
        //メソッド化
        selectMenu:()=>{
            console.log("ヘッダーのメニュー")
        }
    }
})();