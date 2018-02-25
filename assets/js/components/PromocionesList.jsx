import React from 'react'

class PromocionesList extends React.Component {
    constructor() {
        super();
        
        this.state = {
            current_coupons: []
        };
    }

    getCoupons(filters) {
        $.ajax({
            url: '/api/promociones/?' + $.param(filters),
            datatype: 'json',
            cache: false,
            success: (data) => {
                this.setState({current_coupons: data})
            }
        });
    }

    componentWillMount() {
        this.getCoupons({});
    }

    buildItem(promocion) {
        return (
            <div key={ promocion.id } className="col_1_of_4 span_1_of_4">
                <a href={ '/promociones/' + promocion.id } className="b-link-stripe b-animate-go thickbox">
                    <img src={promocion.image} className="img-responsive" alt=""/>
                    <div className="b-wrapper">
                        <h2 className="b-animate b-from-left    b-delay03 ">
                        <span>{promocion.name}</span>
                        <img src={promocion.image} className="img-responsive" alt="" width="70" height="50"/>
                        <p style={{fontSize:'10px'}}>{promocion.description}</p>
                        <button>Ver promo</button>
                        <label> <i className="heart"> </i>{promocion.value}</label>
                        </h2>
                    </div>
                </a>
		    </div>
        );
    }

    filterCoupons(e) {
        let catId = e.target.value;
        let filter = {}
        if (catId) {
            filter = {'category': catId};
        }
        this.getCoupons(filter);
        e.preventDefault();

    }

    render() {
        let items = [],
            cats = [];

        for (let i = 0; i < this.state.current_coupons.length; i++) {
            items.push(this.buildItem(this.state.current_coupons[i]));
        }

        for (let i = 0; i < this.props.categories.length; i++) {
            cats.push(
                <option key={this.props.categories[i].id} value={this.props.categories[i].id}>{ this.props.categories[i].name }</option>
            )
        }

        return (
            <div>
                <div>
                    <label htmlFor="category">Category</label>
                    <select name="category" onChange={this.filterCoupons.bind(this)} id="category">
                        <option value="">Todas</option>
                        {cats}
                    </select>
                </div>
                {items}
            </div>
        )
    }
}

export default PromocionesList;