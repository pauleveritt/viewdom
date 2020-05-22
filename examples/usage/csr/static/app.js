import {createElement, render} from './preact.js'

const TODOS_URL = '/todos'


function create(h, json) {
    if (Array.isArray(json)) {
        const [tag, props, c] = json
        const children = Array.isArray(c) ? c.map(node => create(h, node)) : c
        return h(tag, props, children)
    }
    return json
}

function updateTodos() {
    const target = document.getElementById('message')
    fetch(TODOS_URL)
        .then(response => response.json())
        .then(data => {
                const vdom = create(createElement, data.response)
                render(vdom, target)

            }
        )
}

window.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('update').addEventListener('click', () => {
        updateTodos()
    })
})
