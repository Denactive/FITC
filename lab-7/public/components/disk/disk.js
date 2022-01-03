export default class DiskComponent {
  constructor(root) {
      this.root = root;
  }

  render(props) {
  this.root.insertAdjacentHTML('beforeend', `
    <div class="card" style="width: 300px;">
      <img class="card-img-top" src="${props.src || '../../static/img/disk-icon.png'}" alt="Диск ${props.title}">
      <div class="card-body">
        <h5 class="card-title">${props.title}</h5>
        <p class="card-text">Совсем другая верстка! ${props.description}</p>
      </div>
    </div>
    `);
  }
}
