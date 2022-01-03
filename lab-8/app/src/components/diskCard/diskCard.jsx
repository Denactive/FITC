import diskDefaultImg from '../../static/img/disk-icon.png';
import {Card} from "react-bootstrap";

const DiskCard = (props) =>
 <Card className="card" style={{width: '200px'}}>
    <Card.Img className="card-img-top" src={diskDefaultImg} alt={props.title}/>
    <Card.Body>
      <a className="textStyle" href={`/disk/${props.id}`}>
        <Card.Title>{props.title}</Card.Title>
      </a>
      <div  className="textStyle">
        <Card.Text>
          {props.description}
        </Card.Text>
      </div>
    </Card.Body>
  </Card>;

export default DiskCard;
