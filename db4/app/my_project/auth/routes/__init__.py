from flask import Flask

def register_routes(app: Flask) -> None:

    from .orders.routes_route import route_bp
    from .orders.route_stops_route import route_stop_bp
    from .orders.guides_route import guide_bp
    from .orders.hotels_route import hotel_bp
    from .orders.means_route import mean_bp
    from .orders.schedule_route import schedule_bp
    from .orders.stops_route import stop_bp
    from .orders.subroutes_route import subroute_bp
    from .orders.excursion_route import excursion_bp
    from .orders.city_hotel_route import city_hotel_bp


    app.register_blueprint(city_hotel_bp)
    app.register_blueprint(route_bp)
    app.register_blueprint(route_stop_bp)
    app.register_blueprint(guide_bp)
    app.register_blueprint(hotel_bp)
    app.register_blueprint(mean_bp)
    app.register_blueprint(schedule_bp)
    app.register_blueprint(stop_bp)
    app.register_blueprint(subroute_bp)
    app.register_blueprint(excursion_bp)
