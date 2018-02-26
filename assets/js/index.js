import ReactDOM from 'react-dom'
import React from 'react';
import PromocionesList from './components/PromocionesList';

$(document).ready(() => {
    let reactClasses = {
        'PromocionesList': <PromocionesList />
    };

    $('[data-react-class]').each((index, element) => {
        let container = $(element);
        let props = container.data('react-props');
        let name = container.data('react-class');
        let el = React.cloneElement(
            reactClasses[name],
            props
        )
        ReactDOM.render(el, element);
    });
});