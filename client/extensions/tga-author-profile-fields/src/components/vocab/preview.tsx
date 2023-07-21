import * as React from 'react';

import {IPreviewComponentProps, IVocabularyItem} from 'superdesk-api';

export class VocabularyPreview extends React.PureComponent<IPreviewComponentProps<IVocabularyItem>> {
    render() {
        return (
            <div className="form__row form__row--small-padding">
                <p className="sd-text__normal">
                    {this.props.value.name}
                </p>
            </div>
        );
    }
}
