(function () {
    var factory = function (exports) {
        var lang = {
            name: "ja",
            description: "オープンソースのオンラインMarkdownエディタ。",
            tocTitle: "目次",
            toolbar: {
                undo: "元に戻す（Ctrl+Z）",
                redo: "やり直す（Ctrl+Y）",
                bold: "太字",
                del: "取り消し線",
                italic: "斜体",
                quote: "引用",
                ucwords: "単語の先頭文字を大文字に変換",
                uppercase: "選択したテキストを大文字に変換",
                lowercase: "選択したテキストを小文字に変換",
                h1: "見出し1",
                h2: "見出し2",
                h3: "見出し3",
                h4: "見出し4",
                h5: "見出し5",
                h6: "見出し6",
                "list-ul": "順序なしリスト",
                "list-ol": "順序付きリスト",
                hr: "水平線",
                link: "リンク",
                "reference-link": "参照リンク",
                image: "画像",
                code: "インラインコード",
                "preformatted-text": "整形済みテキスト / コードブロック（タブインデント）",
                "code-block": "コードブロック（複数言語）",
                table: "テーブル",
                datetime: "日時",
                emoji: "絵文字",
                "html-entities": "HTMLエンティティ",
                pagebreak: "改ページ",
                watch: "ウォッチ",
                unwatch: "ウォッチ解除",
                preview: "HTMLプレビュー（Shift + ESCで終了）",
                fullscreen: "全画面表示（ESCで終了）",
                clear: "クリア",
                search: "検索",
                help: "ヘルプ",
                info: "インフォ " + exports.title
            },
            buttons: {
                enter: "入力",
                cancel: "キャンセル",
                close: "閉じる"
            },
            dialog: {
                link: {
                    title: "リンク",
                    url: "アドレス",
                    urlTitle: "タイトル",
                    urlEmpty: "エラー: リンクのアドレスを入力してください。"
                },
                referenceLink: {
                    title: "参照リンク",
                    name: "名前",
                    url: "アドレス",
                    urlId: "ID",
                    urlTitle: "タイトル",
                    nameEmpty: "エラー: 参照名を入力してください。",
                    idEmpty: "エラー: 参照リンクのIDを入力してください。",
                    urlEmpty: "エラー: 参照リンクのアドレスを入力してください。"
                },
                image: {
                    title: "画像",
                    url: "アドレス",
                    link: "リンク",
                    alt: "タイトル",
                    uploadButton: "アップロード",
                    imageURLEmpty: "エラー: 画像のURLアドレスを入力してください。",
                    uploadFileEmpty: "エラー: アップロードする画像を選択してください。",
                    formatNotAllowed: "エラー: 画像ファイルのみアップロードが許可されています。許可されている画像ファイル形式: "
                },
                preformattedText: {
                    title: "整形済みテキスト / コード",
                    emptyAlert: "エラー: 整形済みテキストまたはコードの内容を入力してください。",
                    placeholder: "コーディング中...."
                },
                codeBlock: {
                    title: "コードブロック",
                    selectLabel: "言語: ",
                    selectDefaultText: "コード言語を選択...",
                    otherLanguage: "その他の言語",
                    unselectedLanguageAlert: "エラー: コード言語を選択してください。",
                    codeEmptyAlert: "エラー: コードの内容を入力してください。",
                    placeholder: "コーディング中...."
                },
                htmlEntities: {
                    title: "HTMLエンティティ"
                },
                help: {
                    title: "ヘルプ"
                }
            }
        };


        exports.defaults.lang = lang;
    };

    // CommonJS/Node.js
    if (typeof require === "function" && typeof exports === "object" && typeof module === "object") {
        module.exports = factory;
    }
    else if (typeof define === "function")  // AMD/CMD/Sea.js
    {
        if (define.amd) { // for Require.js

            define(["editormd"], function (editormd) {
                factory(editormd);
            });

        } else { // for Sea.js
            define(function (require) {
                var editormd = require("../editormd");
                factory(editormd);
            });
        }
    }
    else {
        factory(window.editormd);
    }

})();