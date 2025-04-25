import React from 'react';
import './header.css';

interface SearchBoxProps {
    label: string;
    value: string;
    onChange: (value: string) => void;
    placeholder?: string;
};

export const SearchBox = (props: SearchBoxProps)  => {
    return (
        <div className="search-box">
            <label>{props.label}</label>
            <input
                type="text"
                value={props.value}
                onChange={(e) => props.onChange(e.target.value)}
                placeholder={props.placeholder}
            />
        </div>
    );
};
