import React from 'react';
import logo from './logo.svg';
import './header.css';

interface HeaderProps {
    headerinfo: {
      title: string;
    };
  }

export function Header({ headerinfo }: HeaderProps) {
    return (
        <div>
            <div className="top">
                <img src={logo} className="logo" />
                <div className="site-name">歌詞検索アプリ</div>
            </div>
            <div className="main-title">{headerinfo.title}</div>
        </div>
    )
}
