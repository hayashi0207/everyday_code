//即時関数の書き方
//const 〇〇　＝　(アロー関数)();

const footerModule = (()=>{
    //初期化処理
    let counter=0
    //メソッド化
    return{
        countUp:()=>{
            counter +=1
            console.log("現在のカウンタ")
        },
        selectMenu:()=>{
            console.log("フッターのメニュー")
        }
    }
})();