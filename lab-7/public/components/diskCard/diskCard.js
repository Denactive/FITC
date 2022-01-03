export default class DiskCardComponent {
  constructor(root) {
      this.root = root;
  }

  addListeners(data, listener) {
    document
        .getElementById(`click-card-${data.id}`)
        .addEventListener("click", listener);
}

  render(props, listener) {
  this.root.insertAdjacentHTML('beforeend', `
    <div class="card" style="width: 300px;">
      <img class="card-img-top" src="${props.src || '../../static/img/disk-icon.png'}" alt="${props.title}">
      <div class="card-body">
        <h5 class="card-title">${props.title}</h5>
        <p class="card-text">${props.description}</p>
        <button class="btn btn-primary" id="click-card-${props.id}" data-id="${props.id}">Нажми на меня</button>
      </div>
    </div>
    `);
    this.addListeners(props, listener);
  }
}
