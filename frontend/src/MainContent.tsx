import React, { useState } from 'react';
import './maincontent.css';
import {SearchBox} from './SearchBox';

interface MainContentProps {
    searchparams: {
      title: string;
    };
  }

export function MainContent({ searchparams }: MainContentProps) {
    const [title, setTitle] = useState('');
    const [artist, setArtist] = useState('');

    const [lyrics, setLyrics] = useState(' ここに検索結果が表示されます。');

    const searchParams = [
        "検索条件",
        `曲名：${title}`,
        `アーティスト：${artist}`
    ];

    const handleSearch = () => {
        alert(searchParams.join('\n'));
    };

    const handleCopy = () => {
        navigator.clipboard.writeText(lyrics)
            .then(() => alert('歌詞をコピーしました！'))
            .catch((err) => alert('コピーに失敗しました：' + err));
    }

    return (
        <div>
            <div className="search-form">
                <SearchBox label="曲名" value={title} onChange={setTitle} placeholder="曲名を入力"/>
                <SearchBox label="アーティスト" value={artist} onChange={setArtist} placeholder="アーティストを入力"/>
                <button className="search-button" onClick={handleSearch}>検索</button>
            </div>
            <div className="search-result">
                <div className="lyrics-box">
                    <pre>{lyrics}</pre>
                </div>
                <button className="copy-button" onClick={handleCopy}>コピー</button>
            </div>
        </div>
    );
};
