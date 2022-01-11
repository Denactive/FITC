import DiskCardComponent from '../../components/DiskCard/DiskCard.js';
import DiskPage from '../../pages/disk/diskPage.js';
import urls from '../../module/urls.js';
import ajax from '../../module/ajax.js';

export default class MainPage {
  constructor(root) {
      this.root = root;
  }

  get page() {
    return document.getElementById('main-page')
  }

  getData() {
    return ajax.get({url: urls.disks()});
  }

  render() {
    this.root.innerHTML = '';
    this.root.insertAdjacentHTML('beforeend', `
      <div id="main-page" class="d-flex flex-wrap"><div/>
    `);

    this.getData().then(({response}) => {
      response.forEach(element => {
        const diskCard = new DiskCardComponent(this.page)
        diskCard.render(element, (e) => {
          const cardId = e.currentTarget.dataset.id;
          console.log(cardId);
          const diskPage = new DiskPage(this.root, cardId)
          diskPage.render();
        });
      });
    });
  }
}
