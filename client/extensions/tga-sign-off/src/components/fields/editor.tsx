import * as React from 'react';

import {IEditorProps} from '../../interfaces';
import {superdesk} from '../../superdesk';

import {hasUserSignedOff} from '../../utils';

import {Button, ButtonGroup} from 'superdesk-ui-framework/react';
import {SignOffDetails} from '../details';

export class UserSignOffField extends React.Component<IEditorProps> {
    constructor(props: IEditorProps) {
        super(props);

        this.removeSignOff = this.removeSignOff.bind(this);
        this.sendSignOff = this.sendSignOff.bind(this);
    }

    sendSignOff() {
        superdesk.httpRequestJsonLocal({
            method: "POST",
            path: "/api/sign_off_request",
            payload: {
                item_id: this.props.item._id,
                authors: this.props.item.authors,
            }
        });
    }

    removeSignOff() {
        const {confirm} = superdesk.ui;

        confirm('Are you sure you want to remove this publishing sign off?', 'Remove publishing sign off')
            .then((response) => {
                if (response) {
                    superdesk.entities.article.patch(this.props.item, {
                        extra: {
                            ...(this.props.item.extra ?? {}),
                            publish_sign_off: {},
                        }
                    });
                }
            })
    }

    render() {
        const {gettext} = superdesk.localization;
        const {getCurrentUserId} = superdesk.session;
        const isSameUser = getCurrentUserId() === this.props.item.extra?.sign_off_data?.user_id;

        return (
            <div className="sd-display-flex-column">
                <div className="sd-d-flex sd-flex-align-items-center">
                    <SignOffDetails signOff={this.props.item.extra?.sign_off_data} />
                    {!hasUserSignedOff(this.props.item.extra?.sign_off_data) ? (
                        <Button
                            type="warning"
                            icon="warning-sign"
                            text={gettext('Sign Off')}
                            onClick={this.sendSignOff}
                            expand={true}
                            disabled={this.props.readOnly}
                        />
                    ) : (
                        <ButtonGroup align="end">
                            {this.props.readOnly ? null : (
                                <Button
                                    type="default"
                                    text={gettext('Remove')}
                                    icon="trash"
                                    onClick={this.removeSignOff}
                                />
                            )}
                            {(this.props.readOnly || !isSameUser) ? null : (
                                <Button
                                    type="primary"
                                    text={gettext('Edit')}
                                    icon="pencil"
                                    onClick={this.sendSignOff}
                                />
                            )}
                        </ButtonGroup>
                    )}
                </div>
                {!this.props.item.extra?.funding_source?.length ? null : (
                    <div className="sd-display-flex-column sd-margin-l--5 sd-padding-l--0-5 sd-margin-t--1">
                        <label className="form-label form-label--block">Funding Source:</label>
                        <span>{this.props.item.extra.funding_source}</span>
                    </div>
                )}

                {!this.props.item.extra?.affiliation?.length ? null : (
                    <div className="sd-display-flex-column sd-margin-l--5 sd-padding-l--0-5 sd-margin-t--1">
                        <label className="form-label form-label--block">Affiliation:</label>
                        <span>{this.props.item.extra.affiliation}</span>
                    </div>
                )}
            </div>
        );
    }
}
