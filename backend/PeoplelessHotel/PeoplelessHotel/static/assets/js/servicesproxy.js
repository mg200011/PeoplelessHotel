'use strict';

class ServicesProxy {

    async getReservations() {
        const s = new Services();
        return await s.gget("/reservations");
    }


}
