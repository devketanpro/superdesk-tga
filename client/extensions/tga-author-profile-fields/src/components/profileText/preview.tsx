import * as React from 'react';

import {IPreviewComponentProps} from 'superdesk-api';

export class ProfileTextPreview extends React.PureComponent<IPreviewComponentProps<string>> {
    render() {
        return (
            <div className="form__row form__row--small-padding">
                <div dangerouslySetInnerHTML={{__html: this.props.value}} />
            </div>
        );
    }
}
