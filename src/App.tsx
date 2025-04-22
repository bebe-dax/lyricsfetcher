import React from 'react';
import {Header} from './Header';
import {MainContent} from './MainContent';
import './app.css';

function SearchLyrics() {
  const header = {
    title: "Search Lyrics"
  }
  
  const maincontent = {
    title: "hoge"
  }

  return (
    <div className="SearchLyrics">
      <header>
        <Header headerinfo={header}></Header>
      </header>
      <main>
        <MainContent searchparams={maincontent}></MainContent>
      </main>
    </div>
  );
}

export default SearchLyrics;
